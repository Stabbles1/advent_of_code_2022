from part_2 import main


def test_main():
    assert (
        main(
            [
                "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8",
            ]
        )
        == 4
    )
