/*
 * numbering.cpp
 * 백준 2667_단지번호붙이기
 *
 *  Created on: 2019. 12. 27.
 *      Author: 제서윤
 */


#include <iostream>
#include <algorithm>
#define MAX 25
using namespace std;

void dfs(int n, int i, int j, char map[][MAX], bool visited[][MAX], int group, int house[]);

int main(){
	int n;	//지도의 크기
	cin >> n;

	char map[MAX][MAX];
	bool visited[MAX][MAX];
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			cin >> map[i][j];
			visited[i][j] = false;
		}
	}

	int group = 0;
	int house[MAX*MAX] = {};

	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(map[i][j] == '1' && !visited[i][j]){
				house[group]++;
				dfs(n, i, j, map, visited, group, house);
				group++;
			}

	cout << group << endl;
	sort(house, house+group);
	for(int i=0; i<group; i++)
		cout << house[i] << endl;

	return 0;
}

void dfs(int n, int i, int j, char map[][MAX], bool visited[][MAX], int group, int house[]){
	visited[i][j] = true;
	//cout << "visit[" << i << "][" << j << "]" << endl;
	//cout << "how many house in group " << group << "? " << house[group] << endl;
	if(i>=1)
		if(map[i-1][j]=='1' && !visited[i-1][j]){
			house[group]++;
			dfs(n, i-1, j, map, visited, group, house);
		}
	if(j>=1)
		if(map[i][j-1]=='1' && !visited[i][j-1]){
			house[group]++;
			dfs(n, i, j-1, map, visited, group, house);
		}
	if(i<n-1)
		if(map[i+1][j]=='1' && !visited[i+1][j]){
			house[group]++;
			dfs(n, i+1, j, map, visited, group, house);
		}
	if(j<n-1)
		if(map[i][j+1]=='1' && !visited[i][j+1]){
			house[group]++;
			dfs(n, i, j+1, map, visited, group, house);
		}
}
