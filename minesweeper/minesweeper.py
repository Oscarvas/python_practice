MINE = '*'
BLANK = ' '
CELLS = MINE+BLANK

def annotate(minefield: list[str]) -> list:
    # base case
    if not minefield: return []

    if not _valid_minefield(minefield):
        # when the board receives malformed input
        raise ValueError("The board is invalid with current input.")
    
    result = []
    dim_n = len(minefield)
    dim_m = len(minefield[0])
    
    for row_index, row in enumerate(minefield):
        aux_row = ''

        for col_index, col in enumerate(row):
            if col == BLANK:
                mines = _total_mines_around(minefield,
                                            row_index, col_index,
                                            dim_n, dim_m)
                aux_row += str(mines) if mines else BLANK
                continue

            aux_row += col

        result.append(aux_row)    
    
    return result


def _valid_minefield(minefield: list) -> bool:
    ''' An input minefield is valid when:
        - every row has the same length
        - there's only '*' or ' ' for each cell
    '''

    first_row_len = len(minefield[0])

    for row in minefield:
        for cell in row:
            if len(row) != first_row_len or cell not in CELLS:
                return False
    return True

def _total_mines_around (minefield: list,cell_row: int, cell_col: int, dim_row: int, dim_col) -> int:
    '''
    Determine how many mines surround a given cell
    '''

    # check edges
    top_row = cell_row -1 in range(0,dim_row)
    bot_row = cell_row +1 in range(0,dim_row)
    left_col = cell_col -1 in range(0,dim_col)
    right_col = cell_col +1 in range(0,dim_col)

    total_mines = 0

    if top_row:
        total_mines += sum([
            minefield[cell_row -1][cell_col] == MINE,
            left_col and minefield[cell_row -1][cell_col-1] == MINE,
            right_col and minefield[cell_row -1][cell_col+1] == MINE,
        ])
    if bot_row:
        total_mines += sum([
            minefield[cell_row +1][cell_col] == MINE,
            left_col and minefield[cell_row +1][cell_col-1] == MINE,
            right_col and minefield[cell_row +1][cell_col+1] == MINE,
        ])

    total_mines += sum([
        left_col and minefield[cell_row][cell_col-1] == MINE,
        right_col and minefield[cell_row][cell_col+1] == MINE,
    ])


    return total_mines