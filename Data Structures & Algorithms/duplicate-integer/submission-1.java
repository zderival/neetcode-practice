class Solution {
    public boolean hasDuplicate(int[] nums){
    List<Integer> nums2 = new ArrayList<>();
    for(int num: nums){
        if(nums2.contains(num)){
            return true;
        }else{
            nums2.add(num);
        }
    }
    return false;
}
}