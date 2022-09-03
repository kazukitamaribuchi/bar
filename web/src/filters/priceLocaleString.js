import Vue from 'vue'

const priceLocaleString = function (value) {
  let val = Number(value)
  if (val > 99999999) {
      return '99,999,999'
  }
  return val.toLocaleString()
}

export default priceLocaleString
