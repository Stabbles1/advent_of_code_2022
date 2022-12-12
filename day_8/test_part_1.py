from part_1 import main


def test_main():
    assert (
        main(
            [
                "30373",
                "25512",
                "65332",
                "33549",
                "35390",
            ]
        )
    ) == 21
