package hex;

import water.fvec.Frame;

public class ModelMetricsUnsupervised extends ModelMetrics {
  public ModelMetricsUnsupervised(Model model, Frame frame) {
    super(model, frame, Double.NaN);
  }

  public static abstract class MetricBuilderUnsupervised extends MetricBuilder {
  }
}
