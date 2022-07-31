import Vue from 'vue'

const dispNone = function (value) {
  if (!value || value == null || value == '') return '-'
  return value
}

export default dispNone
