/**
 * Problem Link : https://leetcode.com/problems/sum-of-digits-in-base-k/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

int sumBase(int n, int k) {
    int sum=0;
    while(n)
    {
        sum+=n%k;
        n=n/k;
    }
    return sum;
}
