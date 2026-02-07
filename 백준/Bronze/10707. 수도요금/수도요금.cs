using System;

public class Solution
{
    public static void Main(string[] args)
    {
        int A = int.Parse(Console.ReadLine());
        int B = int.Parse(Console.ReadLine());
        int C = int.Parse(Console.ReadLine());
        int D = int.Parse(Console.ReadLine());
        int P = int.Parse(Console.ReadLine());
        
        int X = P * A;
        int Y = (P <= C) ? B : B + D * (P - C);
        
        Console.WriteLine(Math.Min(X, Y));
    }
}