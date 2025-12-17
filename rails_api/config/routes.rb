Rails.application.routes.draw do
  post "/analyze", to: "ai#analyze"
end
