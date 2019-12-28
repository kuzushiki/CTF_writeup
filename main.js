$(function () {
  $('#submit-button').on('click', function () {
    const url = $('#url-input').val()

    $('#error').html('')
    $('#error').removeClass('error')

    $('#url-input').val('')
    $('#content').html('')

    if (!url) {
      $('#error').addClass('error')
      $('#error').html('<p>URLが入力されていません</p>')

      return false
    }

    if (url.match(/pig/)) {
      $('#error').addClass('error')
      $('#error').html('<p>不正なアクセスを検出しました</p>')

      return false
    }

    const params = new URLSearchParams()
    params.append('url', url)

    axios.post('query.php', params)
      .then(function (res) {
        if (!res.data.error) {
          $('#content').html(res.data.content)
        } else {
          $('#error').addClass('error')
          $('#error').append('<p>' + res.data.error + '</p>')
        }
      })
      .catch(function (err) {
        $('#error').addClass('error')
        $('#error').append('<p>通信に失敗しました</p>')
        console.log(err)
      })

    return false
  })
})