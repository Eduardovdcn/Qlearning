import connection as con

def pos_matrix(state):
    plataform = int(state[2:7],2)
    direction = int(state[7:9],2)
    print(f"plataform: {plataform}")
    print(f"Direction: {direction}")
    return ((4 * plataform) + direction)

def define_act():
    pass

def update_util(curr_direction, curr_platarform, next_direction, next_plataform, reward, const_alfa, const_gama):
    return matriz[curr_direction][curr_platarform] + const_alfa*(reward + const_gama*matriz[next_direction][next_plataform] - matriz[curr_direction][curr_platarform])

def main():
    const_alfa = 0.9
    const_gama = 0.5
    end = 0

    connect = con.connect(2037)
    state = 1010000

    for _ in range(50):
        curr_platarform = state[0:6]
        curr_direction = state[6:8]

        act = define_act(curr_direction)
        state, reward = con.get_state_reward(connect, act)

        next_plataform, next_direction = get_next_act()
        

        matriz[curr_direction][curr_platarform] = update_util(matriz, curr_direction, curr_platarform, next_direction, next_plataform, reward, const_alfa, const_gama)
        curr_direction = next_direction
        curr_platarform = next_plataform

        if reward == 300:
            end = 1

        

if __name__=="__main__":
    main()
