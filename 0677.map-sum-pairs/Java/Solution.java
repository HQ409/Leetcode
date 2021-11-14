package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/map-sum-pairs/"></a>
 * 使用树来保存，每个子母保存为一个节点，每个节点保存此节点的值，以及此节点代表前缀的和
 */
class MapSum {
    public Node head = null;

    public MapSum() {
        head = new Node();
    }

    public void insert(String key, int val) {
        Node node = head;
        for (char c : key.toCharArray()) {
            if (node.children[c - 97] == null) {
                node.children[c - 97] = new Node();
                node.children[c - 97].value = 0;
                node.children[c - 97].sum = 0;
            }
            node = node.children[c - 97];
        }
        int valChange = val - node.value;
        node.value=val;
        node = head;
        for (char c : key.toCharArray()) {
            node.sum += valChange;
            node = node.children[c - 97];
        }
        node.sum += valChange;
    }

    public int sum(String prefix) {
        Node node = head;
        for (char c : prefix.toCharArray()) {
            if (node.children[c - 97] == null) {
                return 0;
            }
            node = node.children[c - 97];
        }
        return node.sum;
    }

    class Node {
        int value;
        int sum;
        Node[] children = new Node[26];
    }


    public static void main(String[] s) throws Exception {
        MapSum mapSum = new MapSum();
        mapSum.insert("apple", 3);
        System.out.println(mapSum.sum("ap"));
        mapSum.insert("app", 2);
        System.out.println(mapSum.sum("ap"));

    }
}