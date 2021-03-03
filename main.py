from pytube import YouTube


def downloading():
    print("Waiting .......... 🧭")


def finish():
    print("Download done")


def choose_type():
    print(f"press y if you want it highest resolution , press n if you want it Lowest resolution")
    h_l = input()
    return h_l


def main():
    link = input("Enter youtube Link: ").strip()
    video = YouTube(link, on_progress_callback=downloading())
    print(f"video name : {video.title} ")
    print(f"channel name : {video.author}")
    print("--------------------------------------------------")

    h_l = choose_type()

    if h_l == "y":
        video.streams.filter(type="video").get_highest_resolution().download(output_path="./download")
    else:
        video.streams.filter(type="video").get_lowest_resolution().download(output_path="./download")

    video.register_on_complete_callback(finish())


if __name__ == "__main__":
    try:
        main()

    except:
        print("Something went wrong")

