START_OF_MESSAGE_LENGTH = 14


def main(input):
    start_of_packet_index = 0
    start_of_packet_tracker = []
    for char in input:
        print(start_of_packet_tracker)
        start_of_packet_tracker.append(char)
        start_of_packet_index += 1
        if len(start_of_packet_tracker) > START_OF_MESSAGE_LENGTH:
            start_of_packet_tracker.pop(0)
            if len(set(start_of_packet_tracker)) == START_OF_MESSAGE_LENGTH:
                return start_of_packet_index
    raise Exception("No start of packet found")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read()))
