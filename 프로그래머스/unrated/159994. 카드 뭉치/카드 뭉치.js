function solution(cards1, cards2, goal) {
    let temp1 = [...cards1]
    let temp2 = [...cards2]
    
    let c1 = 0 , c2 = 0;
    for (const g of goal) {
        if (g === temp1[c1]) c1 += 1
        else if (g === temp2[c2]) c2 += 1
        else return "No"
    }
    
    return "Yes"
}