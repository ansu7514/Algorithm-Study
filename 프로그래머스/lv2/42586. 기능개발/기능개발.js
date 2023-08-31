function solution(progresses, speeds) {
    let releases = [];
    
    let prevNum = -1;
    let releaseCnt = 1;
    for (let i = 0; i < progresses.length; i++) {
        let progress = progresses[i];
        let speed = speeds[i];
        
        let due = Math.ceil((100 - progress) / speed);
        
        if(i === 0) {
            prevNum = due;
            continue;
        }
        
        if (prevNum >= due) {
            releaseCnt++;
        } else {
            prevNum = due;
            releases.push(releaseCnt);
            releaseCnt = 1;
        }
    }
    
    if (releaseCnt != 0) releases.push(releaseCnt);
    
    return releases;
}