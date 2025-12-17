require "net/http"
require "json"

class AiController < ApplicationController
  def analyze
    uri = URI("http://127.0.0.1:8000/analyze")

    payload = {
      store_id: params[:store_id],
      question: params[:question]
    }

    http = Net::HTTP.new(uri.host, uri.port)
    request = Net::HTTP::Post.new(uri, { "Content-Type" => "application/json" })
    request.body = payload.to_json

    response = http.request(request)

    render json: JSON.parse(response.body)
  end
end
