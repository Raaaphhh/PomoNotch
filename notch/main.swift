import Cocoa

let app = NSApplication.shared
app.setActivationPolicy(.regular)

guard let screen = NSScreen.main else { exit(1) }

let notchWidth: CGFloat = 350
let notchHeight: CGFloat = 33
let notchX = (screen.frame.width - notchWidth) / 2
let notchY = screen.frame.height - notchHeight

let window = NSWindow(
    contentRect: NSRect(x: notchX + notchWidth / 2, y: notchY, width: 0, height: notchHeight),
    styleMask: [],
    backing: .buffered,
    defer: false
)
window.backgroundColor = .clear
window.isOpaque = false
window.hasShadow = false
window.level = .screenSaver

let notchView = RoundedView(frame: NSRect(x: 0, y: 0, width: notchWidth, height: notchHeight))

if let rightArea = screen.auxiliaryTopRightArea {
    notchView.timerX = rightArea.minX - notchX + 23 // deplacer horizontalement
} else {
    notchView.timerX = notchWidth * 0.65
}

if let leftArea = screen.auxiliaryTopLeftArea {
    notchView.timerLeftX = leftArea.maxX - notchX - 10
} else {
    notchView.timerLeftX = notchWidth * 0.35
}
notchView.leftText = "🍅 Break"

window.contentView = notchView
window.makeKeyAndOrderFront(nil)
app.activate(ignoringOtherApps: true)

let breakDuration = TimeInterval(CommandLine.arguments.count > 1 ? Double(CommandLine.arguments[1]) ?? 0 : 0)

let ctx = NotchContext(window: window, view: notchView, screenWidth: screen.frame.width, y: notchY, width: notchWidth, height: notchHeight)
startAnimation(opening: true, ctx: ctx, breakDuration: breakDuration)

app.run()
