#!/bin/bash

echo "Uninstalling PomoNotch..."

rm -rf "$HOME/.pomonotch"
rm -f "$HOME/.local/bin/pomonotch"

for RC in "$HOME/.zshrc" "$HOME/.bashrc"; do
    if [ -f "$RC" ]; then
        sed -i '' '/# PomoNotch/d' "$RC"
        sed -i '' '/\.local\/bin.*PATH/d' "$RC"
    fi
done

echo "PomoNotch uninstalled."
