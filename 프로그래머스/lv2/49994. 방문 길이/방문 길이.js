function solution(dirs) {
    let pointList = [];
    
    prePoint = [0, 0];
    nowPoint = [0, 0];
    
    dirs.split("").forEach(d => {
        let tempPoint = [...nowPoint];
        if (d === 'U' && nowPoint[1] !== 5) tempPoint[1] += 1
        else if (d === 'D' && nowPoint[1] !== -5) tempPoint[1] -=1
        else if (d === 'R' && nowPoint[0] !== 5) tempPoint[0] +=1
        else if (d === 'L' && nowPoint[0] !== -5) tempPoint[0] -=1
        
        // 이전 점과 현재 점이 동일하면 제외
        if (!(nowPoint[0] === tempPoint[0] && nowPoint[1] === tempPoint[1]))
            pointList.push([nowPoint, tempPoint]);

        prePoint = [...nowPoint];
        nowPoint = [...tempPoint];
    });
    
    let answer = [];
    pointList.forEach(([prePoint, nowPoint]) => {
        let check = false;
        answer.forEach(([pre, now]) => {
            // answer에 동일한 점 있을 경우 제외
            if (pre[0] === prePoint[0] && pre[1] === prePoint[1] && now[0] === nowPoint[0] && now[1] === nowPoint[1])
                check = true;
            
            // answer에 반대로 동일한 점 있을 경우 제외
            if (pre[0] === nowPoint[0] && pre[1] === nowPoint[1] && now[0] === prePoint[0] && now[1] === prePoint[1])
                check = true;
        });
        
        if (!check) answer.push([prePoint, nowPoint]);
    });
    
    return answer.length
}