#!/bin/bash
set -e

INSTALL_DIR="$HOME/.pomonotch"
BIN_DIR="$HOME/.local/bin"

echo "Updating PomoNotch..."

# Check installation
if [ ! -d "$INSTALL_DIR/.git" ]; then
    echo "PomoNotch is not installed. Run install.sh first."
    exit 1
fi

# Save current commit
BEFORE=$(git -C "$INSTALL_DIR" rev-parse --short HEAD)

# Pull latest changes
git -C "$INSTALL_DIR" fetch --quiet
COMMITS_BEHIND=$(git -C "$INSTALL_DIR" rev-list HEAD..origin/main --count 2>/dev/null || echo 0)

if [ "$COMMITS_BEHIND" = "0" ]; then
    echo "Already up to date ($(git -C "$INSTALL_DIR" rev-parse --short HEAD))."
    exit 0
fi

git -C "$INSTALL_DIR" pull --quiet

AFTER=$(git -C "$INSTALL_DIR" rev-parse --short HEAD)

# Update dependencies if requirements.txt changed
if git -C "$INSTALL_DIR" diff "$BEFORE" "$AFTER" --name-only | grep -q "requirements.txt"; then
    echo "Updating dependencies..."
    pip3 install --quiet -r "$INSTALL_DIR/requirements.txt"
fi

# Ensure binary is still executable
chmod +x "$INSTALL_DIR/notch/notch_binary"

# Recreate launcher in case it changed
cat > "$BIN_DIR/pomonotch" << 'EOF'
#!/bin/bash
python3 "$HOME/.pomonotch/main.py" "$@"
EOF
chmod +x "$BIN_DIR/pomonotch"

echo ""
echo "PomoNotch updated: $BEFORE → $AFTER"
echo ""
echo "Changes:"
git -C "$INSTALL_DIR" log "$BEFORE..$AFTER" --oneline
