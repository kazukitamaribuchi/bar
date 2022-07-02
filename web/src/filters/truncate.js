import Vue from 'vue'

const truncate = function (value, num, end) {
  if (!value) return ''
  var e = (end != null) ? end : '...'
  if (value.length >= num) return value.substr(0, num) + e
  return value
}

export default truncate
