import Cocoa

class RoundedView: NSView {
    var timeRemaining: TimeInterval = 0
    var timerX: CGFloat = 0
    var leftText: String = ""
    var timerLeftX: CGFloat = 0

    private let cornerRadius: CGFloat = 12

    override func draw(_ dirtyRect: NSRect) {
        drawNotchShape()
        if timerX > 0 { drawTimer() }
        if timerLeftX > 0 { drawLeftText() }
    }

    private func drawNotchShape() {
        // Black rectangle with flat top and rounded bottom corners
        let r = cornerRadius
        let b = bounds
        let path = NSBezierPath()
        path.move(to: NSPoint(x: b.minX, y: b.maxY))
        path.line(to: NSPoint(x: b.maxX, y: b.maxY))
        path.line(to: NSPoint(x: b.maxX, y: b.minY + r))
        path.appendArc(withCenter: NSPoint(x: b.maxX - r, y: b.minY + r), radius: r, startAngle: 0, endAngle: -90, clockwise: true)
        path.line(to: NSPoint(x: b.minX + r, y: b.minY))
        path.appendArc(withCenter: NSPoint(x: b.minX + r, y: b.minY + r), radius: r, startAngle: -90, endAngle: 180, clockwise: true)
        path.close()
        NSColor.black.setFill()
        path.fill()
    }

    private func drawLeftText() {
        let text = leftText as NSString
        let attrs: [NSAttributedString.Key: Any] = [
            .foregroundColor: NSColor.white,
            .font: NSFont.monospacedDigitSystemFont(ofSize: 13, weight: .medium)
        ]
        let textSize = text.size(withAttributes: attrs)
        text.draw(
            at: NSPoint(x: timerLeftX - textSize.width, y: (bounds.height - textSize.height) / 2 + 1),
            withAttributes: attrs
        )
    }

    private func drawTimer() {
        let minutes = Int(timeRemaining) / 60
        let seconds = Int(timeRemaining) % 60
        let text = String(format: "%02d:%02d", minutes, seconds) as NSString
        let attrs: [NSAttributedString.Key: Any] = [
            .foregroundColor: NSColor.white,
            .font: NSFont.monospacedDigitSystemFont(ofSize: 13, weight: .medium)
        ]
        let textSize = text.size(withAttributes: attrs)
        text.draw(
            at: NSPoint(x: timerX, y: (bounds.height - textSize.height) / 2 + 1),
            withAttributes: attrs
        )
    }
}
