class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> s_string = new HashMap<> ();
        Map<Character,Integer> t_string = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if (!s_string.containsKey(s.charAt(i))){
                s_string.put(s.charAt(i),1);
            }else{
                int increament = s_string.get(s.charAt(i)); 
                increament++;
                s_string.put(s.charAt(i),increament);
            }
        }
        for(int i = 0; i < t.length(); i++){
            if(!t_string.containsKey(t.charAt(i))){
                t_string.put(t.charAt(i),1);
            }else{
                int increament = t_string.get(t.charAt(i));
                increament++;
                t_string.put(t.charAt(i), increament); 
            }
    
        }
        return s_string.equals(t_string);
    }   
}

