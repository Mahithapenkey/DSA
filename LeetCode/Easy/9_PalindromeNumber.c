/**
 * Problem Link : https://leetcode.com/problems/palindrome-number/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(int x) {
    // Negative numbers or numbers ending with 0 (except 0 itself) aren't palindromes
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    
    int reversed = 0;
    while (x > reversed) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    
    // For even digits, x should equal reversed
    // For odd digits, x should equal reversed/10
    return x == reversed || x == reversed / 10;
}
