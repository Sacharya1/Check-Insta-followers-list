# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:40:59 2020

@author: Sampad Acharya
"""
import time


def insta_unfollowed_check(following,followers):

    read_following=following.read()
    read_followers=followers.read()
    split_following=read_following.split("\n")
    split_followers=read_followers.split("\n")
    
    
    following_list=[]
    for i in split_following:
      if "profile picture" in i:
        id=i.split("'s")
        following_list.append(id[0])
        
    
    followers_list=[]
    for i in split_followers:
      if "profile picture" in i:
        id=i.split("'s")
        followers_list.append(id[0])
    
    unfollow_list=[]    
    for i in following_list:
      if i not in followers_list:
        print(i)
        unfollow_list.append(i)
    following.close()
    followers.close()    
    print("\nTotal Runtime: %s mili-seconds" % (float(time.time() - start_time)*1000))    
    following_list.sort()
    followers_list.sort()
    following.close()
    followers.close()    
            
def main():
    global start_time
    start_time = time.time()
    following=open('following.txt')
    followers=open('followers.txt')
    insta_unfollowed_check(following,followers)
    del start_time


if __name__=="__main__":
    main()