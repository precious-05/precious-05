with open('e:/precious-05/README.md', 'r', encoding='utf-8') as f:
    content = f.read()

emojis_to_remove = [
    '🚀 ', '🎯 ', '💡 ', '🛠️ ', '🌐 ', '💻 ', '📊 ', 
    '🍎 ', '🌲 ', '🩺 ', '💊 ', '🌾 ', '💰 ', '🎮 ', '📈 '
]

for emoji in emojis_to_remove:
    content = content.replace(emoji, '')

# Also remove trailing/leading spaces created if any, but since I included a space in the array, it should be clean.

with open('e:/precious-05/README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Emojis removed.")
