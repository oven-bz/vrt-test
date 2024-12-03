# VRT Test

This is a VRT Test answer detection tool. It is designed to be used with the VRT Test image.

The tool is able to detect answers in the VRT Test image and output the answers for evaluation.

## Approach Explanation

We found there are 2 possible approaches for us to analyze the VRT answer sheet.

1. Use normal OCR to detect content and combine it with Large Language Model (LLM) processing to improve the output results from OCR.
2. Use the pre-trained LLM model (e.g., Llama Vision 3.2), which has already been trained to detect the symbols and content accurately.

The results of both approaches are as follows:

1. The first approach results in bad output. The OCR is not able to detect the content accurately, and the LLM model is not able to improve the output.
2. The second approach results in better output. The Llama Vision 3.2 model is able to detect the symbols accurately, but the content is not detected accurately.

After trying both approaches, we found that the second approach is better than the first approach. In conclusion, we will use the second approach to analyze the VRT answer sheet and try to improve the output results.

## Usage

To use the VRT Test answer detection tool, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/oven-bz/vrt-test.git
```

2. Install the required packages:

```shell
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

3. Provide the VRT Test image in the `images` directory.

4. Run the tool:

```shell
python main.py
```

## Output Example

The output of the tool will be displayed in the console. The detected answers will be displayed in the following format:

```json
{
  "role": "assistant",
  "content": "The provided image appears to be a series of questions or prompts, each with multiple-choice answers. The markings include a cross (X), circle (O), and underscore (_). Here is the list of boxes and their corresponding marked answers:\n\n1. X\n2. O\n3. O\n4. X\n5. _\n6. X\n7. O\n8. X\n9. O\n10. X\n11. O\n12. X\n13. O\n14. X\n15. O\n16. X\n17. O\n18. X\n19. O\n20. X\n21. _\n22. X\n23. O\n24. X\n25. _\n26. O\n27. X\n28. O\n29. X\n30. O\n31. X\n32. O\n33. X\n34. O\n35. X\n36. O\n37. X\n38. O\n39. X\n40. O\n41. X\n42. _\n43. O\n44. X\n45. O\n46. X\n47. O\n48. X\n49. O\n50. _\n51. X\n52. O\n53. X\n54. _\n\nThese marked answers can be used to determine the results of a test or survey, depending on how they were intended to be interpreted.\n\nPlease note that the analysis provided is based solely on the image and does not include any external information or context.",
  "images": null,
  "tool_calls": null
}
```
