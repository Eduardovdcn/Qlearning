# Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as con
import constants
import pandas as pd
from pandas import DataFrame


def get_movement(move: int) -> str:
    """
    Returns a string with the movement based on the value of @move parameter
    0: left
    1: right
    2: jump
    """

    if 0 > move or move >= 3:
        raise ValueError(
            'Invalid move value. Only values between 0 and 2 are allowed (inclusive)'
        )

    print('next movement: ', constants.MOVE_MAP[move])
    return constants.MOVE_MAP[move]


def get_next_direction(matriz: str, plataforma: int): 
    biggest = -9999
    direction = -1

    for x in range(3):
        if matriz[x][plataforma] >= biggest: #tem que garantir que as duas variáveis são do mesmo tipo!
            biggest = matriz[x][plataforma]
            direction = x

    return direction


def get_next_platform(state: str) -> int:
    """return next platform based on the current one"""

    print(f'prevstate: {state}')
    direction = int(state[7:9], 2)
    plat = int(state[2:7], 2)
    print(f'next direction: {direction}')
    print(f'next state [plat]: {plat}')

    return (plat << 2) + direction


def load_policy_from_file(file: str) -> DataFrame:
    """Read csv file with default values"""

    return pd.read_csv(file, header=None, sep=' ')


def write_policy_file(df: DataFrame):
    """write df with updated values as a txt file"""
    df.to_csv('resultado.txt', header=None, index=None, mode='w', sep=' ')


def update_util(
    matriz,
    curr_direction,
    curr_platarform,
    next_direction,
    next_plataform,
    reward,
    const_alfa,
    const_gama,
):
    return matriz[curr_direction][curr_platarform] + const_alfa * (
        reward
        + const_gama * matriz[next_direction][next_plataform]
        - matriz[curr_direction][curr_platarform]
    )


def main():
    connect = con.connect(2037)
    state = '1b1010000'
    curr_platarform = int(state[2:7], 2)
    curr_direction = int(state[7:9], 2)
    print(curr_direction)

    matriz = load_policy_from_file('resultado.txt')

    for _ in range(constants.LOOP_ITERATIONS):
        print(curr_direction)
        act = get_movement(curr_direction)
        state, reward = con.get_state_reward(connect, act)

        next_plataform = get_next_platform(state)

        next_direction = get_next_direction(matriz, next_plataform)

        matriz[curr_direction][curr_platarform] = update_util(
            matriz,
            curr_direction,
            curr_platarform,
            next_direction,
            next_plataform,
            reward,
            constants.ALPHA,
            constants.GAMMA,
        )
        curr_direction = next_direction
        curr_platarform = next_plataform

        if reward == 300:   break

    write_policy_file(matriz)

    print('acabou :(')

if __name__ == '__main__':
    main()
