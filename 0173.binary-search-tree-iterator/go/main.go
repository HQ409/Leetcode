/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type BSTIterator struct {
	Vals  []int
	Index int
}

func constructor(root *TreeNode, bstIterator *BSTIterator) {
	if root == nil {
		return
	}
	constructor(root.Left, bstIterator)
	bstIterator.Vals = append(bstIterator.Vals, root.Val)
	constructor(root.Right, bstIterator)
}

func Constructor(root *TreeNode) BSTIterator {
	bstIterator := BSTIterator{Index: -1}
	constructor(root, &bstIterator)
	return bstIterator
}

func (this *BSTIterator) Next() int {
	this.Index++
	ret := this.Vals[this.Index]
	return ret
}

func (this *BSTIterator) HasNext() bool {
	return this.Index+1 < len(this.Vals)
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */