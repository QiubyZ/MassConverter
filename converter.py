import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def convert_file(file_path: Path, output_folder: Path, extension: str) -> None:
    output_file = output_folder / f"{file_path.stem}{extension}"
    command = ["ffmpeg", "-i", str(file_path), str(output_file)]
    subprocess.run(command, check=True)

def main(file_from: str, to_folder: str, extension: str) -> None:
    file_from_path = Path(file_from)
    to_folder_path = Path(to_folder)
    to_folder_path.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor() as executor:
        for file in file_from_path.iterdir():
            if file.is_file() and file.suffix != extension:
                executor.submit(convert_file, file, to_folder_path, extension)

if __name__ == "__main__": 
    print("Mass Converter File (QiubyZhukhi)")
    file_from = input("From File Folder: ")
    to_folder = input("To folder: ")
    extension = input("Convert to Extension: ")
    main(
        file_from,
        to_folder,
        extension,
    )


