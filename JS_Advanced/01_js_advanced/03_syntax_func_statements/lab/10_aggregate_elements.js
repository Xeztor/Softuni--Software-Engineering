function solve(nums) {
    console.log(aggregate(nums, x => x))
    console.log(aggregate(nums, x => 1 / x))
    console.log(aggregate(nums, x => String(x)))

    function aggregate(nums, func) {
        let result = func(nums[0]);

        for (i = 1; i < nums.length; i++){
            result += func(nums[i]);
        }

        return result

    }
}

// solve([2, 4, 8, 16])
