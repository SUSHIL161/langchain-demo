from langchain_demo.chains import build_qa_chain


def test_build_qa_chain_returns_runnable():
    chain = build_qa_chain()
    assert hasattr(chain, "invoke")
