function partition(arr, x){
    let ori = arr;
    let left = list();
    let right = list();
    
    while (!is_null(ori)) {
        let curr = head(ori);
        
        if(curr < x) {
            left = append(left, list(curr));
        } 
        else if (curr > x) {
            right = append(right, list(curr));
        } 
        else {}
        
        ori = tail(ori);
    }
    
    return pair(left, right);
}

function quicksort(arr) {
    if (length(arr) <= 1) {
        return arr;
    } 
    else {
        const piv = head(arr);
        
        const partitions = partition(arr, piv);
        const left = head(partitions);
        const right = tail(partitions);
        
        return append(quicksort(left), pair(piv, quicksort(right)));
    }
    
}

quicksort(list(3, 6, 3, 7, 8 ,9, 2, 1));