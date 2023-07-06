    from nemoguardrails.rails import LLMRails, RailsConfig
    def demo():
        config = RailsConfig.from_path("./config")
        rails = LLMRails(config)
        response = rails.generate(messages=[{
            "role": "user",
            "content": input("Prompt: ")
        }])
        print(response)
    if __name__ == "__main__":
        demo()
