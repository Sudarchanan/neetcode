class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = defaultdict(int)

        for i in nums:

            res[i] +=1

        sorted_dict = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}

        out =[]
        all_values_view = sorted_dict.keys()
        all_values_list = list(all_values_view)
        for i in range(k):
            out.append(all_values_list[i])

        return out
            
