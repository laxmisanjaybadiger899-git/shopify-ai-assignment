class AiController < ApplicationController
  require "net/http"
  require "json"

  def analyze
    uri = URI("http://127.0.0.1:8000/analyze")

    http = Net::HTTP.new(uri.host, uri.port)
    request = Net::HTTP::Post.new(uri.path, { "Content-Type" => "application/json" })

    request.body = {
      text: params[:text]
    }.to_json

    response = http.request(request)

    render json: JSON.parse(response.body)
  end
end
