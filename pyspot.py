import os
import subprocess
import sys

def check_spotdl_installed():
    """Check if spotdl is installed, if not provide installation instructions"""
    try:
        subprocess.run(['spotdl', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_spotdl():
    """Attempt to install spotdl"""
    print("spotdl is not installed. Installing now...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'spotdl', '--break-system-packages'])
        print("spotdl installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install spotdl automatically.")
        print("Please install it manually by running: pip install spotdl --break-system-packages")
        return False

def download_playlist(playlist_url, output_dir):
    """Download songs from Spotify playlist to specified directory"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    # Change to output directory
    original_dir = os.getcwd()
    os.chdir(output_dir)
    
    try:
        print(f"\nDownloading playlist to: {output_dir}")
        print("This may take a while depending on the playlist size...\n")
        
        # Run spotdl command
        result = subprocess.run(
            ['spotdl', playlist_url],
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print("\n✓ Download completed successfully!")
            return True
        else:
            print("\n✗ Download failed. Please check the playlist URL and try again.")
            return False
            
    except Exception as e:
        print(f"\n✗ Error during download: {e}")
        return False
    finally:
        # Return to original directory
        os.chdir(original_dir)

def main():
    print("=" * 50)
    print("Spotify Playlist Downloader made by:Y.S.F")
    print("=" * 50)
    
    # Check if spotdl is installed
    if not check_spotdl_installed():
        if not install_spotdl():
            return
    
    # Get playlist URL from user
    playlist_url = input("\nEnter Spotify playlist URL: ").strip()
    
    if not playlist_url:
        print("Error: No URL provided!")
        return
    
    # Get output directory from user
    output_dir = input("Enter folder path to save songs: ").strip()
    
    if not output_dir:
        print("Error: No directory provided!")
        return
    
    # Expand user path (handles ~/ on Unix)
    output_dir = os.path.expanduser(output_dir)
    
    # Download the playlist
    download_playlist(playlist_url, output_dir)
    
    print(f"\nSongs saved to: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()
