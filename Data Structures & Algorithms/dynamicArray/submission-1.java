class DynamicArray {
    // Actual array
    int[] arr;
    // how many elements are being used
    int size;
    // how many elements can be held at one time
    int capacity;
    public DynamicArray(int capacity) {
        /* Intialize an empty array with the capcity parameter
        when capacity = 0

        1. Check the number given for capacity
            a. If capacity < 0, set it to 0
        2. Set the capacity to the what is given */
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[this.capacity];
    }
    public int get(int i) {
        // Check how many elements are in the array first
        // if the index is more the arraycount - 1 then its invalid.
        // else array.index(i)
        return arr[i];
    }

    public void set(int i, int n) {
        // i is the index were setting to
        // n is the number we are setting
        // Transverse through the array and looking for
        // where i is in the array
        // the set n at array[i]
        arr[i] = n;
    }

    public void pushback(int n) {

        // Resize the array if full
            // wdym resize the array
            // maybe just arr[size]++
            // so check if the array is full first
        // place the element at the new size
            // so set n = arr[size]
        // increament the size
            // size++;
        if(size == capacity){
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        // I need to get the last element in a array
        // I can just return .index(DynamicArray.length() - 1)
        size--;
        return arr[size];
    }

    public void resize() {
        // I need to access the capacity
        // multiply it by 2
        capacity = capacity * 2;
        int[] newArr = new int[capacity];
        for(int i = 0; i < size; i++){
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}