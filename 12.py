
import 'dart:collection';

var buffer = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""";

var lines = buffer.split('\n');

class Node {
  var previousStep;
  int x = 0,y = 0,h = 0,d = 0;
  Node(int x, int y, int h, int d, Node? previousStep) {
    this.x = x;
    this.y = y;
    this.d = d;
    this.h = h;
    this.previousStep = previousStep;
  }
}

var directions = [[1,0],[-1,0],[0,1],[0,-1]];

int main () {
  var starts = <Node>[];
  var dest;
  
  
  
  for (var i = 0; i < lines.length; i++) {
    for (var j = 0; j < lines[i].runes.length; j++) {
      var chars = lines[i].runes.toList();
      if (chars[j] == 83 || chars[j] == 'a'.runes.first) {
        starts.add(Node(i,j,'a'.runes.first,0,null));
      }
      if (chars[j] == 69) {
        lines[i] = lines[i].substring(0, j) + "z" + lines[i].substring(j+1);
        dest = new Node(i,j,'z'.runes.first,0,null);
      }
    } 
  }
  
  int findShortestPath(Node start) {
    
  
  var visited = <List<bool>>[];
    for (var i = 0; i < lines.length; i++) {
      visited.add(List<bool>.filled(lines[i].length, false));
    }
  visited[start.x][start.y] = true;
    
  var queue = Queue<Node>();
  queue.addFirst(start);
  var node;
  while (queue.isNotEmpty) {
    node = queue.removeFirst();
    
    if (node.x == dest.x && node.y == dest.y) {
      return node.d;
    }
    for (var dir in directions) {
      var new_x = node.x + dir[0];
      var new_y = node.y + dir[1];
      if (new_x < 0 || new_y < 0 || new_x >= lines.length || new_y >= lines[0].length) {
        continue;
      }
      

      
      var char = lines[new_x].runes.toList()[new_y];
      
      if (char - node.h <= 1 && !visited[new_x][new_y]) {
        queue.addLast(Node(new_x,new_y,char,node.d+1,node));
        visited[new_x][new_y] = true;
      }
    }
  }
  return 50000;
  }

  var min = -1;  
  for (var start in starts) {
    var steps = findShortestPath(start);
    if (steps < min || min < 0) {
      min = steps;
    }
  }

  print('min: ${min}');
  

  return 0;
}

