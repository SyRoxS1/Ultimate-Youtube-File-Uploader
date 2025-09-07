# Ultimate YouTube File Uploader

It seems like youtube compression got stronger, i recommend using the strong setting for the safety i during testing i got corruption on file using weak safety setting

This program is designed to upload files to YouTube by converting them into videos. The process involves creating images containing the file data, compiling these images into a video, and then uploading the video to YouTube.

## Inspiration

The original idea for this project was inspired by [DvorakDwarf's "Infinite-Storage-Glitch"](https://github.com/DvorakDwarf/Infinite-Storage-Glitch/tree/master/src). However, this project introduces enhancements such as:

- Displaying uploaded files as files within the script.
- Automating the upload process using the YouTube API (limited to 6 videos per day). For bypassing this limitation, I used the work on the [tiktoka-studio-uploader](https://github.com/wanghaisheng/tiktoka-studio-uploader) repo.

## Key Features

1. **YouTubeAsCloud**: 
    - Input a channel URL to list all videos on the channel (via the YouTube API).
    - Select a video to download and convert back into its original file format.
    - While still a work in progress, this feature is functional and may be improved in the future.

2. **File-to-Video and Video-to-File Conversion**:
    - Choose options 1 or 2 in the script to convert files to videos or videos back to files.

3. **Windows Server-Side Automation**:
    - Check the [WindowsServerSide branch](https://github.com/SyRoxS1/Ultimate-Youtube-File-Uploader/tree/main/Srv-Win) (now merged into the main branch) for automation.
    - Automatically convert files placed in a designated folder into videos and upload them to YouTube with the necessary metadata for reverse conversion.

4. **Graphical User Interface (GUI)**:
    - A GUI branch is under development, which will use the API to display channel information and files in a user-friendly interface.

## Installation

> **Important Note**: This code has been tested with Python 3.10.16. Python 3.12 and later versions may cause issues with package installation.

### Steps to Install:

1. Clone the repository:
    ```bash
    git clone https://github.com/SyRoxS1/Ultimate-Youtube-File-Uploader.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Ultimate-Youtube-File-Uploader
    ```

3. Create a virtual environment:
    ```bash
    python -m venv .env
    ```

4. Activate the virtual environment:
    - On Linux/Mac:
      ```bash
      source .env/bin/activate
      ```
    - On Windows:
      ```cmd
      .env\Scripts\activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r notes/requirements.txt
    ```

6. Run the program:
    ```bash
    python main.py
    ```

---
