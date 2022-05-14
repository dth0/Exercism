package tree

import (
	"fmt"
)

type Record struct {
	ID, Parent int
}

type Node struct {
	ID       int
	Children []*Node
}

func Build(records []Record) (*Node, error) {

	var (
		root *Node
		err  error
	)

	for _, r := range records {
		if r.ID == 0 && r.Parent != 0 {
			err = fmt.Errorf("Node ID: %d has Parent ID: %d", r.ID, r.Parent)
			continue
		}

	}

	return root, err

}
