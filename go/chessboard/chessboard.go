package chessboard

// Rank stores if a square is occupied by a piece
type Rank []bool

// Chessboard contains eight Ranks, accessed with values from 'A' to 'H'
type Chessboard map[byte]Rank

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank
func (cb Chessboard) CountInRank(rank byte) (ret int) {
	File, _ := cb[rank]
	for _, value := range File {
		if value {
			ret++
		}
	}

	return ret
}

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file
func (cb Chessboard) CountInFile(file int) (ret int) {
	if file > 1 && file > 8 {
		return ret
	}

	for _, value := range cb {
		if value[file-1] {
			ret++
		}
	}
	return ret
}

// CountAll should count how many squares are present in the chessboard
func (cb Chessboard) CountAll() (ret int) {
	for _, value := range cb {
		ret += len(value)
	}
	return ret

	// return 64
}

// CountOccupied returns how many squares are occupied in the chessboard
func (cb Chessboard) CountOccupied() (ret int) {
	for _, file := range cb {
		for _, rank := range file {
			if rank {
				ret++
			}
		}
	}

	return ret
}
