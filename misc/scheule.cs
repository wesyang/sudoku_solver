/*

We are writing a tool to help users manage their calendars. Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.

Each time is expressed as an integer using 24-hour notation, such as 1200 (12:00), 1530 (15:30), or 800 (8:00).

Sample input:

p1_meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

p2_meetings = [
  ( 0, 844),
  ( 930, 1200),
  (1515, 1546),
  (1600, 2400),
]

p3_meetings = [
  ( 845, 915),
  (1515, 1545),
  (1235, 1245),
]

p4_meetings = [
  ( 1, 5),
  (844, 900),
  (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

Expected output:

findAvailableTimes(schedules1)
 => [  844,  845 ],
    [  915,  930 ],
    [ 1200, 1230 ],
    [ 1500, 1515 ],
    [ 1546, 1600 ]

findAvailableTimes(schedules2)
 => [    0,  845 ],
    [  915, 1230 ],
    [ 1500, 1515 ],
    [ 1545, 2400 ]

findAvailableTimes(schedules3)
    [  900,  930 ],
    [ 1200, 1515 ]

n = number of meetings per schedule
s = number of schedules


*/

using System;
using System.Collections.Generic;
using System.Linq;

/// ignore changes.  It's after interview for completionlist

class Solution {

    static void Print (IEnumerable <int[]> items)
    {
        if (items == null){
            Console.WriteLine ($"Empty");
            return;
        }

         foreach (var i in items){
            Console.WriteLine ($"(start: {i[0]}, end {i[1]} )");
        }
        Console.WriteLine ("------------------");
    }

    static IEnumerable <int []> SortMeetings (int[] [] [] schedule)
    {
        IEnumerable <int []> collection =  schedule[0];
        for (int i = 1; i< schedule.Count(); i++)
        {
            collection = collection.Concat (schedule[i]);
        }
        var sorted = collection.OrderBy (x=> x[0]);
        //Print (sorted);

        return sorted.ToArray();
    }

    static bool InBetween (int[] range, int point) => (range[0] <= point &&  point <= range[1]);
    static int Larger (int a, int b) => a > b? a : b;
    static int Smaller (int a, int b) => a < b? a: b;


    static bool CanMerge (int[] first, int[] next)
    {
        if (first == null)
        {
            return false;
        }

        if(InBetween (first, next[0]) || InBetween (first, next[1]))
        {
            return true;
        }

        if(InBetween (next, first[0]) || InBetween (next, first[1]))
        {
            return true;
        }

        return false;
    }

    static int [] MergeTwo (int[] first, int[] next)
    {
        return new int[] {Smaller (first[0], next[0]), Larger(first[1], next[1])};
    }

    static void Debug (string msg){
        //Console.WriteLine (msg);
    }

    static IEnumerable <int []>  MergeMeetings (IEnumerable <int []> meetings)
    {
        // merge all items in the list into single collection
        // sort new collection
        // loop through new collection to detect if there is overlapping
        // if there is overloapping merge item
        //

        List<int[]> merged = new List<int[]> ();
        foreach (var item in meetings)
        {
            var last = merged.LastOrDefault ();
            var newItem = item;
            if (CanMerge (last, item))
            {
                Debug ($"*** merge ({last[0]} {last[1]}) with ({item[0]} {item[1]})");
                newItem = MergeTwo (last, item);

                Debug ($"*** mergedItem ({newItem[0]} {newItem[1]})");
                merged.Remove(last);
            }
            merged.Add (newItem);
         }

        Debug ("------------------");
        //Print (merged);

        return merged;
    }

    static int [] CreateTimeSlot (int start, int end) => new int[] {start, end};

    static IEnumerable <int []> BuildAvaliableList (IEnumerable <int []> meetingsCloolect)
    {
        var start = 0;
        var result = new List<int[]> ();
        foreach (var item in meetingsCloolect)
        {
            if (start < item[0])
            {
                result.Add ( CreateTimeSlot (start, item[0]) );
            }
            start = item[1];
        }

        var last = meetingsCloolect.LastOrDefault ();
        int endDay = 2400;

        if (last != null && last[1]< endDay)
        {
            result.Add (CreateTimeSlot (last[1], endDay) );
        }
        return result;
    }

    static void Process (int [][][] schedules)
    {
       var sortedMeetings =  SortMeetings (schedules);
       var mergedCollection =  MergeMeetings (sortedMeetings);
       var finalList =  BuildAvaliableList (mergedCollection);
       Print (finalList);
    }

    static void Main(String[] args) {

        int[][] p1Meetings = {
            new int[] {1230, 1300},
            new int[] { 845,  900},
            new int[] {1300, 1500}
        };
        int[][] p2Meetings = {
            new int[] { 0, 844},
            new int[] { 930, 1200},
            new int[] {1515, 1546},
            new int[] {1600, 2400}
        };
        int[][] p3Meetings = {
            new int[] { 845,  915},
            new int[] {1515, 1545},
            new int[] {1235, 1245}
        };
        int[][] p4Meetings = {
            new int[] {    1, 5},
            new int[] {  844, 900},
            new int[] { 1515, 1600}
        };


        int[][][] schedules1 = {p1Meetings, p2Meetings, p3Meetings};
        int[][][] schedules2 = {p1Meetings, p3Meetings};
        int[][][] schedules3 = {p2Meetings, p4Meetings};


      Process (schedules1);
      Process (schedules2);
      Process (schedules3);

    }
}
