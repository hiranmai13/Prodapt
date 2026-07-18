let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];

let passed = 0;
let failed = 0;

for (let i=0; i<marks.length;i++){
    if (marks[i]>=50){
        console.log(`Student ${i+1}: ${marks[i]} - Pass`);
        passed++;
    }
    else{
        console.log(`Student ${i+1}: ${marks[i]} - Fail`);
        failed++;
    }
}

console.log("\nTotal Passed:", passed);
console.log("Total Failed:",failed);
console.log("Highest Score: ",Math.max(...marks));
console.log("Lowest Marks: ", Math.min(...marks));