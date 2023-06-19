/**
 * @file Two_Sum.c
 * @author djmekki (djallal.me)
 * @brief 
 * @version 0.1
 * @date 2023-06-19
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include <stdlib.h>
/*
 * Note: The returned array must be malloced, assume caller call free()
*/

int	*twoSum(int *nums, int numsSize, int target, int *returnSize)
{
	int i = 0;
	int j;
	int *ret = malloc(sizeof(int) * 2);
	while (i < numsSize)
	{
		j = i + 1;
		while (j < numsSize)
		{
			if (nums[i] + nums[j] == target)
			{
				*returnSize = 2;
				ret[0] = i;
				ret[1] = j;
				return (ret);
			}
			++j;
		}
		++i;
	}
	*returnSize = 0;
	return(NULL);
}
