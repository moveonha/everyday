void main() {
  var nums = {1, 2, 3, 4};
  Set<int> n_nums = {1, 2, 3, 4};
  nums.add(1);
  nums.add(1);
  nums.add(1);
  nums.add(1); //nothing changes, list = list, sets = tuple.
}
