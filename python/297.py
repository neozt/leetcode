# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        result = []
        current_level = [root]
        has_next_level = True
        while has_next_level:
            temp = []
            has_next_level = False
            for node in current_level:
                result.append(node.val if node else None)
                temp.append(node.left if node else None)
                temp.append(node.right if node else None)
                if node and (node.left or node.right):
                    has_next_level = True

            current_level = temp

        return ','.join(map(lambda x: str(x), result))



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        input = list(map(lambda x: None if x == 'None' else int(x), data.split(',')))

        result = [None] * len(input)
        for i, val in enumerate(input):
            if val is None:
                continue

            result[i] = TreeNode(val)
            if i > 0:
                parent = (i - 1) // 2
                if (i - 1) % 2 == 0:
                    result[parent].left = result[i]
                else:
                    result[parent].right = result[i]

        return result[0]




# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

# [1,2,3,null,null,4,5]


root = None
# root = TreeNode(
#     1,
#     TreeNode(2),
#     TreeNode(
#         3,
#         TreeNode(4),
#         TreeNode(
#             5,
#         )
#     )
# )

serialized = ser.serialize(root)
print(serialized)
deserialized = deser.deserialize(serialized)
print(ser.serialize(deserialized))
# ans = deser.deserialize(ser.serialize(root))

print()
