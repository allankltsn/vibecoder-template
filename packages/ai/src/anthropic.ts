import Anthropic from "@anthropic-ai/sdk";
import type { LLMMessage, LLMResponse } from "./types";

export function createAnthropicClient(): Anthropic {
  return new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
}

export async function claudeComplete(
  messages: LLMMessage[],
  model = "claude-opus-4-5",
  maxTokens = 4096,
): Promise<LLMResponse> {
  const client = createAnthropicClient();
  const response = await client.messages.create({
    model,
    max_tokens: maxTokens,
    messages: messages.map(({ role, content }) => ({ role, content })),
  });

  const content = response.content[0];
  if (content.type !== "text") throw new Error("Unexpected response type");

  return {
    content: content.text,
    model: response.model,
    usage: {
      inputTokens: response.usage.input_tokens,
      outputTokens: response.usage.output_tokens,
    },
  };
}
