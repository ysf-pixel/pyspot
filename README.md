# 🎵 Spotify Playlist Downloader

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)

**A simple, interactive Python script to download entire Spotify playlists**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [FAQ](#-faq)

</div>

---

## ✨ Features

- 🎯 **Simple & Interactive** - Just paste your playlist URL and choose where to save
- 📦 **Auto-Installation** - Automatically installs dependencies if missing
- 🎨 **High Quality** - Downloads with proper metadata, album art, and tags
- 📁 **Smart Directory Handling** - Creates folders automatically if they don't exist
- 🐧 **Arch Linux Ready** - Special handling for Arch's pip restrictions

## 🚀 Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ysf-pixel/spotify-playlist-downloader.git
cd spotify-playlist-downloader

# Run the script (it will install dependencies automatically)
python spotify_downloader.py
```

### Manual Dependency Installation

**For most Linux distributions and macOS:**
```bash
pip install spotdl
```

**For Arch Linux:**
```bash
pip install spotdl --break-system-packages
```

**Or use pipx (recommended for Arch):**
```bash
sudo pacman -S python-pipx
pipx install spotdl
```

## 📖 Usage

1. **Run the script:**
   ```bash
   python spotify_downloader.py
   ```

2. **Enter your Spotify playlist URL when prompted:**
   ```
   Enter Spotify playlist URL: https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
   ```

3. **Specify where to save the songs:**
   ```
   Enter folder path to save songs: ~/Music/MyPlaylist
   ```

4. **Sit back and relax!** ☕
   The script will download all tracks with metadata and album art.

### Example

```bash
$ python spotify_downloader.py

==================================================
Spotify Playlist Downloader
==================================================

Enter Spotify playlist URL: https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
Enter folder path to save songs: ~/Music/ChillVibes

Downloading playlist to: /home/user/Music/ChillVibes
This may take a while depending on the playlist size...

✓ Download completed successfully!

Songs saved to: /home/user/Music/ChillVibes
```

## 🎯 Requirements

- Python 3.7 or higher
- Internet connection
- Valid Spotify playlist URL

## 🔧 How It Works

This script uses [spotdl](https://github.com/spotDL/spotify-downloader) under the hood, which:

1. Fetches playlist metadata from Spotify
2. Searches for matching tracks on YouTube Music
3. Downloads high-quality audio
4. Embeds proper metadata and album artwork

## ❓ FAQ

**Q: Is this legal?**  
A: This tool is for personal use only. Please respect copyright laws and artist rights.

**Q: Where do the songs come from?**  
A: Songs are downloaded from YouTube Music based on Spotify metadata.

**Q: What audio quality can I expect?**  
A: Typically 128-256 kbps, depending on source availability.

**Q: Can I download a single song instead of a playlist?**  
A: Yes! Just paste a Spotify track URL instead of a playlist URL.

**Q: The script says spotdl is not found, but I installed it!**  
A: Make sure spotdl is in your PATH. If you used pipx, it should handle this automatically.

## 🐛 Troubleshooting

**Issue: "spotdl: command not found"**
- Try running: `pip install spotdl --break-system-packages` (Arch Linux)
- Or use pipx: `pipx install spotdl`

**Issue: Permission denied when creating directory**
- Make sure you have write permissions to the specified path
- Try using a different directory like `~/Music/`

**Issue: Download fails for specific songs**
- Some songs may not be available on YouTube Music
- The script will continue downloading other tracks

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
Made with Python by some one who is sick of ads

</div>
