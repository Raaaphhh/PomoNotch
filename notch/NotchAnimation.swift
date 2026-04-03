import Cocoa

struct NotchContext {
    let window: NSWindow
    let view: RoundedView
    let screenWidth: CGFloat
    let y: CGFloat
    let width: CGFloat
    let height: CGFloat

    var originX: CGFloat { (screenWidth - width) / 2 }
}

func startAnimation(opening: Bool, ctx: NotchContext, breakDuration: TimeInterval = 0) {
    let fps: TimeInterval = 60
    let steps = Int(0.4 * fps)
    var step = 0

    Timer.scheduledTimer(withTimeInterval: 1.0 / fps, repeats: true) { timer in
        step += 1
        let progress = easeOut(Double(step) / Double(steps))
        let currentWidth = ctx.width * CGFloat(opening ? progress : 1 - progress)
        let currentX = (ctx.screenWidth - currentWidth) / 2

        ctx.window.setFrame(NSRect(x: currentX, y: ctx.y, width: currentWidth, height: ctx.height), display: true)
        ctx.view.frame = NSRect(x: 0, y: 0, width: currentWidth, height: ctx.height)
        ctx.view.needsDisplay = true

        guard step >= steps else { return }
        timer.invalidate()

        if opening {
            ctx.window.setFrame(NSRect(x: ctx.originX, y: ctx.y, width: ctx.width, height: ctx.height), display: true)
            ctx.view.frame = NSRect(x: 0, y: 0, width: ctx.width, height: ctx.height)
            startCountdown(ctx: ctx, breakDuration: breakDuration)
        } else {
            NSApplication.shared.terminate(nil)
        }
    }
}

private func startCountdown(ctx: NotchContext, breakDuration: TimeInterval) {
    ctx.view.timeRemaining = breakDuration
    ctx.view.needsDisplay = true

    var elapsed: TimeInterval = 0
    Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { timer in
        elapsed += 1
        ctx.view.timeRemaining = max(0, breakDuration - elapsed)
        ctx.view.needsDisplay = true
        if elapsed >= breakDuration {
            timer.invalidate()
            startAnimation(opening: false, ctx: ctx)
        }
    }
}

private func easeOut(_ t: Double) -> Double {
    1 - pow(1 - t, 3)
}
