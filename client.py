# Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as conn
import constants


def get_movement(move: int) -> str:
    """
    Returns a string with the movement based on the value of @move parameter
    0: left
    1: right
    2: jump
    """

    if 0 <= move or move >= 3:
        raise ValueError(
            'Invalid move value. Only values between 0 and 2 are allowed (inclusive)'
        )

    return constants.MOVE_MAP[move]


def get_next_platform(state: str) -> int:
    """return next platform based on the current one"""

    print(f'prevstate: {state}')
    direction = int(state[7:9], 2)
    plat = int(state[2:7], 2)
    print(f'next direction: {direction}')
    print(f'next state [plat]: {plat}')

    return (plat << 2) + direction
