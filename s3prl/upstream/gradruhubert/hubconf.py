from .expert import UpstreamExpert as _UpstreamExpert

def gradruhubert(ckpt, model_config, **kwargs):
    """
    RuHuBERT model

    Args:
        ckpt: 
            The checkpoint path for loading the model weights.
        model_config:
            The yaml config path for constructing the model.
    """
    return _UpstreamExpert(ckpt, model_config, **kwargs)
